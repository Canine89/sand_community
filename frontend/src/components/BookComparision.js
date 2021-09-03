const BookComparision = ({ isbns }) => {
  console.log(isbns);
  return (
    <>
      <div className="flex flex-row space-x-4 items-center pl-5 py-4 bg-red-400">
        <div className="text-white font-extrabold">
          <span>비교하고 싶은 책의 ISBN을 입력하세요</span>
          <button
            value="이지스퍼블리싱"
            className="rounded-md ml-4 mr-2 p-2 hover:bg-purple-700 bg-red-600 text-sm text-white font-semibold border-gray-200"
          >
            이지스퍼블리싱
          </button>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-4 pt-4"></div>
    </>
  );
};

export default BookComparision;
