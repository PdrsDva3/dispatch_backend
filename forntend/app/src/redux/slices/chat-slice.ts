import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Message {
	id: string;
	text: string;
	timestamp: string;
	sender: 'user' | 'bot';
}

interface ChatState {
	messages: Message[];
	isLoading: boolean;
	error: string | null;
}

const initialState: ChatState = {
	messages: [],
	isLoading: false,
	error: null,
};

const chatSlice = createSlice({
	name: 'chat',
	initialState,
	reducers: {
		addMessage: (state, action: PayloadAction<Message>) => {
			state.messages.push(action.payload);
		},
		setLoading: (state, action: PayloadAction<boolean>) => {
			state.isLoading = action.payload;
		},
		setError: (state, action: PayloadAction<string | null>) => {
			state.error = action.payload;
		},
	},
});

export const { addMessage, setLoading, setError } = chatSlice.actions;
export default chatSlice.reducer;
