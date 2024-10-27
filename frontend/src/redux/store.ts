import chatReducer from './slices/chat-slice.ts';
import streamReducer from './slices/stream-slice.ts';
import {configureStore} from '@reduxjs/toolkit';

export const store = configureStore({
	reducer: {
		chat: chatReducer,
		stream: streamReducer,
	},
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch
