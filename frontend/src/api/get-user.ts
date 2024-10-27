export const postUser = async (email: string, password: string) => {
	const response = await fetch('/api/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({ email, password }),
	});

	if (!response.ok) {
		throw new Error('Failed to fetch user data');
	}

	return response.json();
};
