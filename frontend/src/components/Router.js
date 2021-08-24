import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import Auth from 'routes/Auth';
import Home from 'routes/Home';
import BookStrategy from 'components/BookStrategy';
import Navigation from 'components/Navigation';

const AppRouter = ({ userInfo }) => {
  return (
    <Router>
      {userInfo && <Navigation />}
      <Switch>
        {userInfo ? (
          <>
            <Route exact path="/">
              <Home userInfo={userInfo} />
            </Route>
            <Route exact path="/strategy">
              <BookStrategy />
            </Route>
          </>
        ) : (
          <Route exact path="/">
            <Auth />
          </Route>
        )}
      </Switch>
    </Router>
  );
};

export default AppRouter;
