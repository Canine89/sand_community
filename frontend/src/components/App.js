import AppRouter from 'components/Router';

import { useState, useEffect } from 'react';
import { authService } from 'fbase';

function App() {
  const [userInfo, setUserInfo] = useState({});
  const authorizeUserList = {
    'phk707@easyspub.co.kr': 'Kv7ptg84ErWjc5LzTq3ikkoBD783',
    'phk707kr@gmail.com': 'DmpMpuj0jlZFPdpmAEutSyKnGtm2',
  };

  useEffect(() => {
    authService.onAuthStateChanged((user) => {
      if (user) {
        if (authorizeUserList[user.email]) {
          let _userInfo = {
            displayName: user.displayName,
            uid: user.uid,
            email: user.email,
            photoURL: user.photoURL,
            isAuthorize: true,
          };
          setUserInfo(_userInfo);
        } else {
          let _userInfo = {
            displayName: user.displayName,
            uid: user.uid,
            email: user.email,
            photoURL: user.photoURL,
            isAuthorize: false,
          };
          setUserInfo(_userInfo);
        }
      } else {
        setUserInfo(null);
      }
    });
  }, []);

  return <AppRouter userInfo={userInfo} />;
}

export default App;
