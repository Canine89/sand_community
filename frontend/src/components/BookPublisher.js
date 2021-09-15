import { useState, useEffect } from 'react';
import GraphWithBooks from 'components/GraphWithBooks';

const BookPublisher = () => {
  const [groupingData, setGroupingData] = useState([]);
  const [renderingData, setRenderingData] = useState([]);
  const [fetchUrl, setFetchUrl] = useState('');

  useEffect(() => {
    fetch(fetchUrl)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        const groupedData = groupBy(_json, (data) => data.book.isbn);
        setGroupingData(groupedData);
      });
  }, [fetchUrl]);

  useEffect(() => {
    const arrayData = [];
    groupingData.forEach((value, key, mapObj) => {
      arrayData.push(value);
    });
    setRenderingData(arrayData);
  }, [groupingData]);

  const onClickHander = (e) => {
    const value = e.target.value;
    const _fetchUrl =
      'http://127.0.0.1:8000/book/publisher/?publisher=' + value;
    setFetchUrl(_fetchUrl);
  };

  const groupBy = (list, keyGetter) => {
    const map = new Map();
    list.forEach((item) => {
      const key = keyGetter(item);
      const collection = map.get(key);
      if (!collection) {
        map.set(key, [item]);
      } else {
        collection.push(item);
      }
    });
    return map;
  };

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          <span>보고 싶은 출판사를 선택하세요</span>
          <button
            value="이지스퍼블리싱"
            onClick={onClickHander}
            className="rounded-md ml-4 mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            이지스퍼블리싱
          </button>
          <button
            value="한빛미디어"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            한빛미디어
          </button>
          <button
            value="인사이트(insight)"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            인사이트
          </button>
          <button
            value="제이펍"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            제이펍
          </button>
          <button
            value="길벗"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            길벗
          </button>
          <button
            value="비제이퍼블릭(BJ퍼블릭)"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            비제이퍼블릭(BJ퍼블릭)
          </button>
          <button
            value="루비페이퍼"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            루비페이퍼
          </button>
          <button
            value="생능출판사"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            생능출판사
          </button>
          <button
            value="골든래빗"
            onClick={onClickHander}
            className="rounded-md mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            골든래빗
          </button>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-4 pt-4">
        {renderingData.slice(0, 18).map((_array, _index) => {
          return (
            <div>
              <GraphWithBooks _array={_array} key={_index} />
            </div>
          );
        })}
      </div>
    </>
  );
};

export default BookPublisher;
