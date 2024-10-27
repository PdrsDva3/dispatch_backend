// import './MonitoringPage.scss';
import {
	Box,
	CardMedia,
	Chip,
	Container,
	Divider,
	Grid2,
	IconButton,
	List,
	ListItem,
	Typography,
} from '@mui/material';
import arrow_left from '../../assets/svg/arrow_left.svg';
import {useNavigate} from 'react-router-dom';
import {Chat} from '../../components/Chat/Chat.tsx';
import {useDispatch, useSelector} from 'react-redux';
import {useEffect} from 'react';
import type {RootState} from '../../redux/store.ts';

export const MonitoringPage = () => {
	const navigate = useNavigate();

	const handleSectionClick = () => {
		navigate('/');
	};

	const dispatch = useDispatch();
	const imageData = useSelector((state: RootState) => state.stream.imageData);

	useEffect(() => {
		dispatch({type: 'stream/connect'});
	}, [dispatch]);


	return (
		<Grid2 container spacing={2} sx={{ px: 10, mt: 2 }}>
			<Grid2 size={8} >
				<Container sx={{
					p: 0,
					display: 'flex',
					alignItems: 'center',
					justifyContent: 'flex-start',
					bgcolor: 'common.white',
					borderRadius: '10px',
					boxShadow: '5px 5px 15px rgba(0, 0, 0, 0.16)',
				}}>
					<IconButton onClick={handleSectionClick} color="primary" sx={{ p: 1 }}>
						<img src={arrow_left} alt="Перейти" />
					</IconButton>
					<Chip label="Мониторинг" sx={{ fontSize: 20, borderRadius: '10px', p: 0 }} component="h2"
					      color="error" />
				</Container>
				<Box sx={{
					backgroundColor: 'white',
					borderRadius: '10px',
					overflow: 'hidden',
					mt: 2,
					boxShadow: '5px 5px 15px rgba(0, 0, 0, 0.16)',
				}}>
					<CardMedia
						id="videoStream"
						height='600vh'
						component="img"
						src={imageData ? `data:image/jpeg;base64,${imageData}` : ''}
						alt="image stream"
						sx={{ borderRadius: '10px', boxShadow: '5px 5px 15px rgba(0, 0, 0, 0.16)' }}
					/>
				</Box>
			</Grid2>
			<Grid2 size={4} sx={{display:'flex', justifyContent:'space-between', flexDirection:'column'}}>
				<Chat/>
				<Container sx={{ display:'flex', flexDirection:'column', justifyContent:'flex-start',
					backgroundColor: 'white',
					borderRadius: '10px',
					overflow: 'hidden',
					pt: 2,
					boxShadow: '5px 5px 15px rgba(0, 0, 0, 0.16)',
				}}>

					<Chip label="Текущая информация" sx={{ alignSelf:'flex-start', fontSize: 20, borderRadius: '10px', p:0 }}
					      component="h2"
					      color="error"
								 />
					<Divider sx={{ py: 1 }} />
					<List>
						<ListItem sx={{
							display: 'flex',
							flexDirection: 'column',
							alignItems: 'center',
							gap: 1,
							justifyContent: 'flex-end',
							p: 0,
						}}>
							<Container sx={{ p: 0, display:"flex", gap:1,  }}>
								<Typography component="span" variant="h6" sx={{ color: 'common.black' }}>
									Тип:
								</Typography>
								<Typography
									component="p"
									variant="h6"
									sx={{ color: 'blueGray.main' }}
								>
									погрузочный кран
								</Typography>
							</Container>
							<Container sx={{ p: 0, display:"flex", gap:1 }}>
								<Typography component="span" variant="h6" sx={{ color: 'common.black' }}>
									Кол-во:
								</Typography>
								<Typography
									component="p"
									variant="h6"
									sx={{ color: 'blueGray.main' }}
								>
									1 единица
								</Typography>

							</Container>
							<Container sx={{ pt:2, display:"flex", gap:1,  }}>
								<Typography component="span" variant="h6" sx={{ color: 'common.black' }}>
									Тип:
								</Typography>
								<Typography
									component="p"
									variant="h6"
									sx={{ color: 'blueGray.main' }}
								>
									погрузочный кран
								</Typography>
							</Container>
							<Container sx={{ p: 0, display:"flex", gap:1 }}>
								<Typography component="span" variant="h6" sx={{ color: 'common.black' }}>
									Кол-во:
								</Typography>
								<Typography
									component="p"
									variant="h6"
									sx={{ color: 'blueGray.main' }}
								>
									1 единица
								</Typography>

							</Container>
						</ListItem>

					</List>

				</Container>
			</Grid2>
		</Grid2>
	);
};
