import { authService, firebaseInstance } from 'fbase';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGoogle } from '@fortawesome/free-brands-svg-icons';

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
        <button
          className="rounded-md border px-2 py-1 mx-2 font-semibold text-white bg-green-400"
          onClick={onSocialClick}
          name="google"
        >
          구글로 로그인 <FontAwesomeIcon icon={faGoogle} />
        </button>
      </div>
    </div>
  );
};

export default Auth;
