import { store } from '../redux/store';
import { addMessage } from '../redux/slices';

interface Message {
	id: string;
	text: string;
	timestamp: string;
}

const socket = new WebSocket('ws://localhost:8001');

socket.addEventListener('open', () => {
	console.log('WebSocket connected');
});

socket.addEventListener('message', (event) => {
	const message: Message = JSON.parse(event.data);
	store.dispatch(addMessage(message));
});

socket.addEventListener('close', () => {
	console.log('WebSocket disconnected');
});

export default socket;
