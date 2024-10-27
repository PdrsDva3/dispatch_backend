import './LoginPage.scss';
import big_train from '../../assets/svg/bigTrain.svg';
import ellipse from '../../assets/svg/Ellipse.svg';
import line_left_bottom from '../../assets/svg/LineLeftBottom.svg';
import line_left_top from '../../assets/svg/LineLeftTop.svg';
import line_right_bottom from '../../assets/svg/LineRightBottom.svg';
import rectangle_left_bottom from '../../assets/svg/RectangleLeftBottom.svg';
import rectangle_left_top from '../../assets/svg/RectangleLeftTop.svg';
import rectangle_right_top from '../../assets/svg/RectangleRightTop.svg';
import small_train from '../../assets/svg/smallTrain.svg';
import tree from '../../assets/svg/Tree.svg';
import subtracts from '../../assets/svg/Subtract.svg';

import { Button, TextField, Typography } from '@mui/material';

import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { EMPTY_FORM_DATA, FORM_SCHEME } from "../../constants";
import type { IFormLogin } from '../../interfaces';
import { useNavigate } from 'react-router-dom';

export const LoginPage = () => {
	const navigate = useNavigate();

	// useForm
	const {
		register,
		handleSubmit,
		reset,
		formState: { errors },
	} = useForm<IFormLogin>({
		defaultValues: EMPTY_FORM_DATA,
		resolver: yupResolver(FORM_SCHEME),
	});

	const onSubmit = (formData: IFormLogin) => {
		navigate('/');
		reset(EMPTY_FORM_DATA);
		console.log(formData);
	};


	return (
		<section className='login'>
			<div className="main_wrapper">
				<div>
					<img className="big_train" src={big_train} alt="" />
					<img src={ellipse} alt="" className="ellipse" />
					<img src={line_left_bottom} alt="" className="line_left_bottom" />
					<img src={line_left_top} alt="" className="line_left_top" />
					<img src={line_right_bottom} alt="" className="line_right_bottom" />
					<img src={rectangle_left_bottom} alt="" className="rectangle_left_bottom" />
					<img src={rectangle_left_top} alt="" className="rectangle_left_top" />
					<img src={rectangle_right_top} alt="" className="rectangle_right_top" />
					<img src={small_train} alt="" className="small_train" />
					<img src={tree} alt="" className="tree" />
					<img src={subtracts} alt="" className="subtracts" />
				</div>
				{/*<div className="form_wrapper">*/}
					<form className="login_form" onSubmit={handleSubmit(onSubmit)}>
						<Typography className='title'
						            id='title'
						            variant='h3'
						            sx={{ mt: 3 }}
						>
							Вход в систему
						</Typography>

						<TextField
							id='login_user_email'
							label='Почта'
							sx={[{ color: 'secondary.main', width:"0.9", backgroundColor:"common.white",

						}, { '&:autofill': { backgroundColor: 'common.white' } }]}
							{...register("email")}
							type="email"
							name="email"
							error={!!errors.email}
							helperText={errors.email?.message}

						/>

						<TextField
							id='login_user_password'
							label='Пароль'
							sx={{ color: 'secondary.main', width:"0.9" }}
							{...register("password")}
							type="password"
							name="password"
							error={!!errors.password}
							helperText={errors.password?.message}

						/>
						<Button type="submit" className='login__btn' variant="contained" sx={{borderRadius:"10px", px:5 , py:1.5, mt:"auto", mb:3}}>Войти</Button>
					</form>
			</div>
		</section>
	);
};
