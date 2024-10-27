import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { addMessage } from '../redux/slices';

export const useSSE = (url: string) => {
	const dispatch = useDispatch();

	useEffect(() => {
		const eventSource = new EventSource(url);

		eventSource.onmessage = (event) => {
			dispatch(addMessage(event.data));
		};

		eventSource.onerror = () => {
			console.error('EventSource failed.');
			eventSource.close();
		};

		return () => {
			eventSource.close();
		};
	}, [url, dispatch]);
};


