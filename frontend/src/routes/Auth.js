import { authService, firebaseInstance } from 'fbase';

const Auth = () => {
  const onSocialClick = async (event) => {
    let provider;
    if (event.target.name === 'google') {
      provider = new firebaseInstance.auth.GoogleAuthProvider();
    }
    const data = await authService.signInWithPopup(provider);
  };

  return (
    <div>
      <div>
        <button onClick={onSocialClick} name="google">
          continue with google
        </button>
      </div>
    </div>
  );
};

export default Auth;
