import './NotFoundPage.scss'
import error_img from '../../assets/svg/error.svg'
import { Link } from 'react-router-dom';

export const NotFoundPage = () => {
	return (
		<section className="not-found-page">
			<img src={error_img} alt="error" className='not-found-page__image' />
			<p className="not-found-page__number">404</p>
			<p className="not-found-page__text">Страница не найдена</p>
			<Link className="not-found-page__back" to='/'>вернуться на главную</Link>
		</section>
	);
};
