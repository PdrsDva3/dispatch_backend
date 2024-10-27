import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface StreamState {
	imageData: string | null;
}

const initialState: StreamState = {
	imageData: null,
};

const streamSlice = createSlice({
	name: 'stream',
	initialState,
	reducers: {
		setImageData(state, action: PayloadAction<string>) {
			state.imageData = action.payload;
		},
	},
	extraReducers: (builder) => {
		builder.addCase('stream/connect', (state) => {
			const ws = new WebSocket('ws://localhost:8000/ws');
			ws.onmessage = (event) => {
				const imageData = event.data;
				state.imageData = imageData;
			};
			ws.onopen = () => console.log('WebSocket connection opened');
			ws.onclose = () => console.log('WebSocket connection closed');
			ws.onerror = (error) => console.error('WebSocket error:', error);
		});
	},
});

export const { setImageData } = streamSlice.actions;
export default streamSlice.reducer;
