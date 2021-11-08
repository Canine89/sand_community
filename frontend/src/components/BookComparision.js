import { useState, useEffect } from 'react';
import DataTable from 'react-data-table-component';

const BookComparision = () => {
  const [pubRenderingData, setPubRenderingData] = useState([]);
  const [tagsRenderingData, setTagsRenderingData] = useState([]);

  const pub_columns = [
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
    {
      name: '집계 기준(종수)',
      selector: 'number_of_book',
      sortable: 'true',
      hide: 'md',
    },
  ];

  const tag_columns = [
    {
      name: '#번호',
      selector: 'tagNum',
      sortable: 'true',
    },
    {
      name: '태그 이름',
      selector: 'tagName',
      sortable: 'true',
    },
    {
      name: '개수',
      selector: 'tagCount',
      sortable: 'true',
      hide: 'md',
    },
  ];

  useEffect(() => {
    fetch(
      'http://175.211.105.9:8000/book/publisher/status/' +
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
        console.log(_json);
        const datas = _json.map((data) => {
          return {
            publisher: data.book__publisher,
            sales_point_sum: data.sales_point_sum,
            sales_point_avg: Math.round(data.sales_point_avg),
            rank_avg: Math.round(data.rank_avg),
            number_of_book: data.number_of_book,
          };
        });
        setPubRenderingData(datas);
      });
  }, []);

  useEffect(() => {
    fetch('http://localhost:8000/book/count/tags/')
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        const datas = _json.map((data, index) => {
          return {
            tagNum: index + 1,
            tagName: data.tagName,
            tagCount: data.tagCount,
          };
        });
        setTagsRenderingData(datas);
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
          data={pubRenderingData}
          noHeader
          columns={pub_columns}
          pagination
          fixedHeader
          responsive
          dense
        />
      </div>

      <div className="flex flex-row space-x-4 items-center pl-5 py-2 bg-green-300">
        <div className="text-white font-extrabold">
          <span>카테고리 현황</span>
        </div>
      </div>

      <div className="ag-theme-alpine pt-4">
        <DataTable
          data={tagsRenderingData}
          noHeader
          columns={tag_columns}
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
