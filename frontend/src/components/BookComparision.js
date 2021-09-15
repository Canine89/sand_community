import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';
import GraphWithIsbnOptions from 'components/GraphWithIsbnOptions';
import Loading from './Loading';

const BookComparision = () => {
  const [renderingData, setRenderingData] = useState([]);
  const [book1, setBook1] = useState(-1);
  const [book2, setBook2] = useState(-1);
  const [isbnData1, setIsbnData1] = useState([]);
  const [isbnData2, setIsbnData2] = useState([]);
  const [title1, setTitle1] = useState('');
  const [title2, setTitle2] = useState('');

  const columns = [
    {
      name: '출판사',
      selector: 'publisher',
      sortable: 'true',
    },
    {
      name: '판매지수 합',
      selector: 'sales_point_sum',
      sortable: 'false',
    },
    {
      name: '판매지수 평균',
      selector: 'sales_point_avg',
      sortable: 'true',
      hide: 'md',
    },
    {
      name: '순위 평균',
      selector: 'rank_avg',
      sortable: 'true',
      hide: 'md',
    },
  ];

  const book1OnChangeHandler = (e) => {
    console.log(e.target.value);
    setBook1(e.target.value);
  };

  const book2OnChangeHandler = (e) => {
    console.log(e.target.value);
    setBook2(e.target.value);
  };

  const onClickHander = (e) => {
    console.log('http://127.0.0.1:8000/book/isbn/?id=' + book1);
    console.log('http://127.0.0.1:8000/book/isbn/?id=' + book2);
    fetch('http://127.0.0.1:8000/book/isbn/?id=' + book1)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        setIsbnData1(_json);
        setTitle1(_json[0].book.title);
      });

    fetch('http://127.0.0.1:8000/book/isbn/?id=' + book2)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        setIsbnData2(_json);
        setTitle2(_json[0].book.title);
      });
  };

  useEffect(() => {
    fetch(
      'http://127.0.0.1:8000/book/publisher/status/' +
        '?year=' +
        new Date().getFullYear().toString() +
        '&month=' +
        (new Date().getMonth() + 1).toString() +
        '&day=' +
        new Date().getDate().toString(),
    )
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        // console.log(_json);
        const datas = _json.map((data) => {
          return {
            publisher: data.book__publisher,
            sales_point_sum: data.sales_point_sum,
            sales_point_avg: data.sales_point_avg,
            rank_avg: data.rank_avg,
          };
        });
        setRenderingData(datas);
      });
  }, []);

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          <span>쓸데없는 비교 차트 업데이트 중</span>
        </div>
      </div>

      <div className="flex flex-row space-x-4 items-center pl-5 py-2 bg-green-300">
        <div className="text-white font-extrabold">
          <span>출판사 지표</span>
        </div>
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

      <div className="flex flex-row space-x-4 items-center pl-5 py-2 bg-green-300">
        <div className="text-white font-extrabold">
          <span>경쟁 도서 비교 지표(ISBN 입력, 지금은 2개만 가능)</span>
        </div>
      </div>

      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-white">
        <div className="text-red-800">도서 1</div>
        <div>
          <input
            className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
            name="book1"
            onChange={book1OnChangeHandler}
          />
        </div>
        <div className="text-red-800">도서 2</div>
        <div>
          <input
            className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
            name="book2"
            onChange={book2OnChangeHandler}
          />
        </div>
        <button
          className="rounded-md border px-2 py-1 font-semibold text-white bg-green-400"
          onClick={onClickHander}
        >
          비교!
        </button>
      </div>

      <div>
        <div className="grid grid-cols-2 gap-4">
          <div>
            {isbnData1.length > 0 ? (
              <GraphWithIsbnOptions isbnData={isbnData1} title={title1} />
            ) : (
              <Loading />
            )}
          </div>
          <div>
            {isbnData2.length > 0 ? (
              <GraphWithIsbnOptions isbnData={isbnData2} title={title2} />
            ) : (
              <Loading />
            )}
          </div>
        </div>
      </div>
    </>
  );
};

export default BookComparision;
