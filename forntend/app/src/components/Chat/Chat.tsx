import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../../redux/store.ts';
import { useSSE } from '../../hooks/use-sse.ts';
import { Box, Button, Chip, Container, Divider, TextField } from '@mui/material';
import { addMessage } from '../../redux/slices';
import { API_URL } from '../../api/config.ts';
import sendlogo from '../../assets/svg/send.svg'

export const Chat: React.FC = () => {

	const [inputValue, setInputValue] = useState<string>('');
	const messages = useSelector((state: RootState) => state.chat.messages);
	const dispatch = useDispatch();

	useSSE('http://localhost:5000/events');

	const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		setInputValue(event.target.value);
	};

	const handleSendMessage = async () => {
		if (inputValue.trim() === '') return;

		try {
			const response = await fetch( `${API_URL}/message`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ message: inputValue }),
			});

			if (!response.ok) {
				throw new Error('Failed to send message');
			}

			const data = await response.json();
			dispatch(addMessage(data.message)); // Добавляем сообщение в Redux
			setInputValue(''); // Очищаем поле ввода
		} catch (error) {
			console.error('Error sending message:', error);
		}
	};

	return (
		<Container sx={{ display: "flex",justifyContent:'space-between' , flexDirection: "column", gap: 1, bgcolor: "common.white", boxShadow: "5px 5px 15px rgba(0, 0, 0, 0.16)", borderRadius: "10px", py: 2 , height:'50vh'}}>
			<Box sx={{display:'flex', flexDirection:'column', justifyContent:'space-between', gap:1}}>
				<Chip label="Чат-бот"  sx={{ alignSelf: "flex-start", borderRadius: "10px", backgroundColor: "primary.main", color: 'common.white' }} />
				<Divider />
			</Box>

			{/*<ul>*/}
			{/*	{messages.map((msg, index) => (*/}
			{/*		<li key={index}>{msg}</li>*/}
			{/*	))}*/}
			{/*</ul>	*/}
			<ul>
				{messages.map(() => (
					<li >message</li>
				))}
			</ul>
			<Box sx={{ display: 'flex', gap: 1, mt: 2 }}>
				<TextField
					sx={{ color: 'secondary.main'}}
					fullWidth
					variant="outlined"
					placeholder="Введите сообщение..."
					value={inputValue}
					onChange={handleInputChange}
				/>
				<Button  onClick={handleSendMessage} sx={{borderRadius:'50%'}}>
					<img src={sendlogo} alt="" />
				</Button>
			</Box>
		</Container>
	);
};
