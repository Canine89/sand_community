const Home = ({ userInfo }) => {
  console.log(userInfo);
  return (
    <>
      <span>{userInfo.displayName}님 반갑습니다.</span>
      {userInfo.isAuthorize
        ? ''
        : '이 메시지가 보이면 관리자에게 승인을 요청해 주세요.'}
    </>
  );
};

export default Home;
