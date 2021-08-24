import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';
import DataTableExtensions from 'react-data-table-component-extensions';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCat, faLocationArrow } from '@fortawesome/free-solid-svg-icons';

const BookStrategy = () => {
  const [data, setData] = useState([]);
  const [renderingData, setRenderingData] = useState([]);
  const [keyword, setKeyword] = useState('');
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
      cell: (row) => {
        return (
          <div>
            {row.title}{' '}
            <a href={row.url}>
              <FontAwesomeIcon icon={faLocationArrow} href={row.url} />
            </a>
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
    fetch('http://localhost:8000/book/')
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
          data.title.toLowerCase().includes(keyword.toLowerCase()) ||
          data.publisher.toLowerCase().includes(keyword.toLowerCase()) ||
          data.tags.toLowerCase().includes(keyword.toLowerCase())
        );
      }),
    );
  }, [keyword]);

  const onChangeHandler = (e) => {
    setKeyword(e.target.value);
  };

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-200">
        <div className="text-red-800">검색어</div>
        <div>
          <input
            className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
            name="keyword"
            value={keyword}
            onChange={onChangeHandler}
          />
        </div>
      </div>

      <div className="ag-theme-alpine">
        <DataTableExtensions
          columns={columns}
          data={renderingData}
          filter={false}
        >
          <DataTable
            data={renderingData}
            noHeader
            columns={columns}
            pagination
            fixedHeader
            responsive
            dense
          />
        </DataTableExtensions>
      </div>
    </>
  );
};

export default BookStrategy;
