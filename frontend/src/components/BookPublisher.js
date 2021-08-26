import { useState, useEffect } from 'react';

const BookPublisher = () => {
  const [renderingData, setRenderingData] = useState([]);
  const [fetchUrl, setFetchUrl] = useState('');

  useEffect(() => {
    fetch(fetchUrl)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        // console.log(_json);
        const groupedData = groupBy(_json, (data) => data.book.isbn);
        setRenderingData(groupedData);
      });
  }, [fetchUrl]);

  useEffect(() => {
    console.log(renderingData);
    renderingData.forEach((value, key, mapObj) => {
      console.log(value);
    });
  }, [renderingData]);

  const onClickHander = (e) => {
    const value = e.target.value;
    const _fetchUrl =
      'http://192.168.0.81:8000/book/publisher/?publisher=' + value;
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
        </div>
      </div>
    </>
  );
};

export default BookPublisher;
