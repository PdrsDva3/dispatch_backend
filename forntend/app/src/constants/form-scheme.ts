import * as yup from 'yup';

export const FORM_SCHEME = yup.object().shape({
	email: yup.string().required("Field shouldn't be empty").email('Invalid email.'),
	password: yup
		.string()
		.required("Field shouldn't be empty")
		.min(3, 'Password should contain more than 3 characters.')
		.max(20, 'Password should contain no more than 20 chars'),
});
