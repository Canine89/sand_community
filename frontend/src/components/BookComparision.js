import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';

const BookComparision = () => {
  const [data, setData] = useState([]);
  const [renderingData, setRenderingData] = useState([]);

  const columns = [
    {
      name: '출판사',
      selector: 'publisher',
      sortable: 'true',
      maxWidth: '150px',
      hide: 'md',
    },
    {
      name: '판매지수 합',
      selector: 'sales_point_sum',
      sortable: 'false',
      maxWidth: '10px',
      hide: 'md',
    },
    {
      name: '판매지수 평균',
      selector: 'sales_point_avg',
      sortable: 'true',
      maxWidth: '10px',
    },
    {
      name: '순위 평균',
      selector: 'rank_avg',
      sortable: 'true',
      maxWidth: '10px',
      hide: 'lg',
    },
  ];

  useEffect(() => {
    console.log(
      'http://192.168.0.81:8000/book/publisher/status/' +
        '?year=' +
        new Date().getFullYear().toString() +
        '&month=' +
        new Date().getMonth().toString() +
        '&day' +
        new Date().getDate().toString(),
    );
    fetch(
      'http://192.168.0.81:8000/book/publisher/status/' +
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
        console.log(datas);
        // setData(datas);
        // setRenderingData(datas);
      });
  }, []);

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          <span>쓸데없는 비교 차트 업데이트 중</span>
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
    </>
  );
};

export default BookComparision;
