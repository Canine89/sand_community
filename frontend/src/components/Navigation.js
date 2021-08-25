import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <div className="flex flex-row space-x-1 py-4 pl-4 bg-red-100 items-center">
      <div className="py-1 px-2 text-red-800">
        <Link to="/">🏠 홈</Link>
      </div>
      <div className="py-1 px-2 text-red-800">
        <Link to="/strategy">🥷 전략실</Link>
      </div>
      <div className="py-1 px-2 text-red-800">
        <Link to="/strategy/publisher">👩‍🔬 이지스퍼블리싱 스탯</Link>
      </div>
    </div>
  );
};

export default Navigation;
