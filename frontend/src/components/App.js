import AppRouter from 'components/Router';

import { useState, useEffect } from 'react';
import { authService } from 'fbase';

function App() {
  const [userInfo, setUserInfo] = useState({});
  const authorizeUserList = {
    'phk707@easyspub.co.kr': 'Kv7ptg84ErWjc5LzTq3ikkoBD783',
    'phk707kr@gmail.com': 'DmpMpuj0jlZFPdpmAEutSyKnGtm2',
    "leesue@easyspub.co.kr": "ycMYfMpeEtbMQuIahsAVqb7la8I3",
    "sgwoo@easyspub.co.kr": "Xctr4dgiQmhJ1GBU6BxwbIQxDZ12",
    "butterfly741@easyspub.co.kr": "x3VcdG2s2NVp3HPJja407XbtyDX2",
    "imsb@easyspub.co.kr": "vYuQKJupDDeNhWNKlWdfNkEAhOQ2",
    "pyk707@gmail.com": "vpLis4bB9lgbWjlRlypLioQT7SW2",
    "inho@easyspub.co.kr": "kfBwo8QvcFOydbSM4JGPCXfS9jE2",
    "junghyun.park@easyspub.co.kr": "g1MfCFViJKfsWjaAxaPYJLSygVw2",
    "ri7951@easyspub.co.kr": "efLkimn0QGawsWW0RXB3kjfi6G63",
    "jiyeong8011@gmail.com": "96d3iypijaTK2AjwHPswASpO9NX2",
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
