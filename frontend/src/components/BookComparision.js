import { useState } from 'react';

const BookComparision = () => {
  const [isbn, setIsbn] = useState(0);
  const [isbnDatas, setIsbnDatas] = useState([]);
  const [titles, setTitles] = useState('');

  const onClickHandler = (e) => {
    fetch('http://localhost:8000/book/isbn/?id=' + isbn)
      .then((response) => {
        return response.json();
      })
      .then((_json) => {
        console.log(_json);
      });
  };

  const onChangeHandler = (e) => {
    console.log(e.target.value);
  };

  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          <span>비교하고 싶은 책의 ISBN을 입력하세요</span>
        </div>
        <div>
          <input
            className="rounded-md border text-sm text-gray-600 pl-2 py-1 mr-4 font-semibold border-gray-200"
            name="isbn"
            onChange={onChangeHandler}
          />
        </div>
        <div>
          <button
            className="rounded-md ml-4 mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
            onClick={onClickHandler}
          >
            추가
          </button>
        </div>
      </div>

      <div className="grid grid-cols-3 gap-4 pt-4"></div>
    </>
  );
};

export default BookComparision;
