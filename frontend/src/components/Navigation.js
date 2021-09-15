import { Link } from 'react-router-dom';
import { authService } from 'fbase';
import { useHistory } from 'react-router-dom';

const Navigation = ({ userInfo }) => {
  const history = useHistory();

  const onLogOutClick = () => {
    authService.signOut();
    history.push('/');
  };

  return (
    <div className="flex flex-row space-x-1 py-4 pl-4 bg-red-100 items-center">
      <div className="py-1 px-2 text-red-800">
        <Link to="/">🏠 홈</Link>
      </div>
      {userInfo.isAuthorize ? (
        <>
          <div className="py-1 px-2 text-red-800">
            <Link to="/strategy">🔬 전략실</Link>
          </div>
          <div className="py-1 px-2 text-red-800">
            <Link to="/comparision">⚗ 각종 테이블</Link>
          </div>
          <div className="py-1 px-2 text-red-800">
            <Link to="/publisher">🧐 출판사</Link>
          </div>
        </>
      ) : (
        ''
      )}
      <div className="py-1 px-2 text-green-800">
        <span onClick={onLogOutClick}>🖐 로그아웃</span>
      </div>
    </div>
  );
};

export default Navigation;
