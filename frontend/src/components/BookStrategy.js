import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faLocationArrow,
  faFileExcel,
  faClone,
} from '@fortawesome/free-solid-svg-icons';
import { CSVLink } from 'react-csv';
import GraphWithIsbn from 'components/GraphWithIsbn';
import { CopyToClipboard } from 'react-copy-to-clipboard';
import Loading from './Loading';
import ReactTooltip from 'react-tooltip';

const BookStrategy = () => {
  const [data, setData] = useState([]);
  const [renderingData, setRenderingData] = useState([]);
  const [searchKeyword, setSearchKeyword] = useState('');
  const [isbnData, setIsbnData] = useState([]);
  const [title, setTitle] = useState('');
  const [gridSize, setGridSize] = useState('grid grid-cols-1 gap-4');

  const columns = [
    {
      name: '순위',
      selector: 'rank',
      sortable: 'true',
      maxWidth: '10px',
    },
    {
      name: '판매지수',
      selector: 'sales_point',
      sortable: 'false',
      maxWidth: '10px',
    },
    {
      name: '제목',
      selector: 'title',
      sortable: 'true',
      maxWidth: '400px',
      cell: (row, index) => {
        return (
          <div>
            <span
              data-tip
              data-for="title"
              onClick={onClickTitleHandler}
              id={row.isbn}
              value={row.title}
            >
              {row.title}
            </span>
            <ReactTooltip id="title">
              <span>제목을 누르면 그래프가 나타납니다.</span>
            </ReactTooltip>
            <a
              target="_blank"
              href={row.url}
              data-tip
              data-for="url"
              className="pl-2"
            >
              <FontAwesomeIcon icon={faLocationArrow} href={row.url} />
            </a>
            <ReactTooltip id="url">
              <span>yes24 사이트로 이동합니다.</span>
            </ReactTooltip>
            <CopyToClipboard
              text={row.isbn}
              data-tip
              data-for="isbn"
              className="pl-2"
            >
              <button>
                <FontAwesomeIcon icon={faClone} />
              </button>
            </CopyToClipboard>
            <ReactTooltip id="isbn">
              <span>isbn을 복사합니다.</span>
            </ReactTooltip>
          </div>
        );
      },
    },
    {
      name: '출판사',
      selector: 'publisher',
      sortable: 'true',
      maxWidth: '150px',
      hide: 'md',
    },
    {
      name: '쪽',
      selector: 'page',
      sortable: 'false',
      maxWidth: '10px',
      hide: 'md',
    },
    {
      name: '가격',
      selector: 'right_price',
      sortable: 'true',
      maxWidth: '10px',
    },
    {
      name: '태그',
      selector: 'tags',
      sortable: 'true',
      maxWidth: '400px',
      hide: 'lg',
    },
  ];

  useEffect(() => {
    fetch('http://127.0.0.1:8000/book/')
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        // console.log(_json);
        const datas = _json.map((data) => {
          return {
            title: data.book.title,
            author: data.book.author,
            isbn: data.book.isbn,
            page: data.book.page,
            publisher: data.book.publisher,
            publish_date: data.book.publish_date,
            right_price: data.book.right_price,
            tags: data.book.tags.reduce((acc, curr) => {
              return acc + ', ' + curr;
            }),
            url: data.book.url,
            rank: data.rank,
            sales_point: data.sales_point,
          };
        });
        setData(datas);
        setRenderingData(datas);
      });
  }, []);

  useEffect(() => {
    setRenderingData(
      data.filter((data) => {
        return (
          data.title.toLowerCase().includes(searchKeyword.toLowerCase()) ||
          data.publisher.toLowerCase().includes(searchKeyword.toLowerCase()) ||
          data.tags.toLowerCase().includes(searchKeyword.toLowerCase())
        );
      }),
    );
  }, [searchKeyword]);

  const onClickTitleHandler = (e) => {
    fetch('http://127.0.0.1:8000/book/isbn/?id=' + e.target.id)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        setIsbnData(_json);
        setTitle(e.target.textContent);
      });
  };

  const onChangeHandler = (e) => {
    setSearchKeyword(e.target.value);
  };

  const onChangeGridSizeHandler = (e) => {
    const gridSize = 'grid grid-cols-' + e.target.value + ' gap-4';
    setGridSize(gridSize);
  };

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          {new Date().getFullYear().toString() +
            '년 ' +
            (new Date().getMonth() + 1).toString() +
            '월 ' +
            new Date().getDate().toString() +
            '일'}
        </div>
      </div>

      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-white">
        <div className="text-red-800">검색어</div>
        <div>
          <input
            className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
            name="searchKeyword"
            value={searchKeyword}
            onChange={onChangeHandler}
          />
        </div>
        <CSVLink
          data={renderingData}
          filename={
            (new Date().getMonth() + 1).toString() +
            '월' +
            new Date().getDate().toString() +
            '일_' +
            'excel_data_' +
            searchKeyword +
            '.xls'
          }
          target="_blank"
        >
          <FontAwesomeIcon icon={faFileExcel} className="mr-2" />
          엑셀 다운로드
        </CSVLink>
      </div>

      <div className="ag-theme-alpine pt-4">
        <DataTable
          data={renderingData}
          noHeader
          columns={columns}
          pagination
          fixedHeader
          responsive
          dense
        />
      </div>

      <div>
        <div className={gridSize}>
          <div>
            {isbnData.length > 0 ? (
              <>
                <div>
                  <span className="text-green-800 extra-bold">
                    그래프 크기 변경 옵션
                  </span>
                  <input
                    className="rounded-md border px-2 py-1 mx-2 font-semibold text-white bg-green-400"
                    type="button"
                    value="1"
                    onClick={onChangeGridSizeHandler}
                  />
                  <input
                    className="rounded-md border px-2 py-1 font-semibold text-white bg-green-400"
                    type="button"
                    value="2"
                    onClick={onChangeGridSizeHandler}
                  />
                </div>
                <GraphWithIsbn isbnData={isbnData} title={title} />
              </>
            ) : (
              <Loading />
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default BookStrategy;
