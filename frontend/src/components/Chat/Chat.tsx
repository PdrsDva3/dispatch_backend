// src/components/Chat.tsx
import React from 'react';
import {useSelector} from 'react-redux';
import {RootState} from '../../redux/store.ts';
import {
	Avatar,
	Chip,
	Container,
	Divider,
	List,
	ListItem,
	ListItemAvatar,
	ListItemText,
	Typography,
} from '@mui/material';
import type {IMessage} from '../../interfaces';

export const Chat: React.FC = () => {
	const messages = useSelector((state: RootState) => state.chat.messages);

	return (
		<Container sx={{
			display: 'flex',
			flexDirection: 'column',
			gap: 2,
			bgcolor: 'background.paper',
			boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
			borderRadius: '12px',
			p: 3,
			height: '50vh',
			overflowY: 'hidden',
		}}>
			<Chip label="Чат-бот" sx={{
				alignSelf: 'flex-start',
				borderRadius: '8px',
				backgroundColor: 'primary.main',
				color: 'white',
			}}/>
			<Divider sx={{my: 2}}/>

			<List sx={{flexGrow: 1, overflowY: 'auto'}}>
				{messages.map((msg: IMessage, index: number) => (
					<ListItem key={index} alignItems="flex-start">
						<ListItemAvatar>
							<Avatar alt="Bot" src="/static/images/avatar/1.jpg"/>
						</ListItemAvatar>
						<ListItemText
							primary={<Typography variant="body1" component="p">{msg.text}</Typography>}
							secondary={
								<Typography
									sx={{display: 'inline'}}
									component="span"
									variant="body2"
									color="text.primary"
								>
									{new Date(msg.timestamp).toLocaleTimeString()}
								</Typography>
							}
						/>
					</ListItem>
				))}
			</List>
		</Container>
	);
};
