import AppRouter from 'components/Router';

import { useState, useEffect } from 'react';
// import { authService } from 'fbase';

function App() {
  const [userInfo, setUserInfo] = useState({ displayName: '🥷닌자너구리' });

  // useEffect(() => {
  //   authService.onAuthStateChanged((user) => {
  //     if (user) {
  //       let _userInfo = {
  //         displayName: user.displayName,
  //         uid: user.uid,
  //         email: user.email,
  //         photoURL: user.photoURL,
  //       };
  //       setUserInfo(_userInfo);
  //     } else {
  //       setUserInfo(null);
  //     }
  //   });
  // }, []);

  return <AppRouter userInfo={userInfo} />;
}

export default App;
