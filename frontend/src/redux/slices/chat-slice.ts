import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import type {IMessage} from '../../interfaces';


interface ChatState {
	messages: IMessage[];
}

const initialState: ChatState = {
	messages: [],
};

const chatSlice = createSlice({
	name: 'chat',
	initialState,
	reducers: {
		addMessage: (state, action: PayloadAction<IMessage>) => {
			state.messages.push(action.payload);
		},
	},
});

export const {addMessage} = chatSlice.actions;
export default chatSlice.reducer;
