const Home = ({ userInfo }) => {
  console.log(userInfo);
  return <span>{userInfo.displayName}님 반갑습니다.</span>;
};

export default Home;
