import { useState } from 'react';
import GraphWithIsbnNoOptions from 'components/GraphWithIsbnNoOptions';
import Loading from 'components/Loading';

const IsbnSearchGraph = () => {
  const [book1, setBook1] = useState(-1);
  const [isbnData1, setIsbnData1] = useState([]);
  const [title1, setTitle1] = useState('');
  const [gridSize, setGridSize] = useState('grid grid-cols-1 gap-4');

  const book1OnChangeHandler = (e) => {
    setBook1(e.target.value);
  };

  const onIsbnClickHander = (e) => {
    fetch('http://175.211.105.9:8000/book/isbn/?id=' + book1)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        setIsbnData1(_json);
        setTitle1(_json[0].book.title);
      });
  };

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-2 bg-green-400">
        <div className="text-white font-extrabold">
          <span>ISBN 검색 그래프</span>
        </div>
      </div>
      <div className="flex flex-row space-x-4 items-center pl-5 py-2 bg-green-100">
        <div className="font-extrabold">
          <span>ISBN</span>
          <span className="pl-4">
            <input
              className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
              name="book1"
              onChange={book1OnChangeHandler}
            />
            <button
              className="rounded-md border px-2 py-1 font-semibold text-white bg-green-400"
              onClick={onIsbnClickHander}
            >
              검색!
            </button>
          </span>
        </div>
      </div>
      <div className={gridSize + ' p-2'}>
        <div>
          {isbnData1.length > 0 ? (
            <GraphWithIsbnNoOptions isbnData={isbnData1} title={title1} />
          ) : (
            <Loading />
          )}
        </div>
      </div>
    </>
  );
};

export default IsbnSearchGraph;
