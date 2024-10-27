import React from 'react';
import { CustomPaper } from '../../reusable';
import { Box, List, ListItem, Typography } from '@mui/material';
import avatar from '../../../assets/svg/avatar.svg';
import backlogo from '../../../assets/svg/backGroundPersonInfo.svg';
import '../PersonalInformationPaper/PersonalInformationPaper.scss';


export const PersonalInformationPaper: React.FC<{hasButton:boolean;}> = ({hasButton}) => {
	return (
		<CustomPaper
			hasButton={hasButton}
			title="Личные данные"
			// navigationPath='/reports'
			className="personal__info elevate--hover"
		>

			<Box
				sx={{display:'flex', alignItems:'center', gap:1}}
			>
				<img src={avatar} alt="" />
				<Typography
					variant="h5"

				>
					Горин Илья Сергеевич
				</Typography>
			</Box>
			<List>
				<ListItem sx={{display:'flex', flexDirection:'row', gap:1}}>
					<Typography component="span" variant="h6">
						Должность:
					</Typography>
					<Typography
						variant="h6"
						sx={{color:'blueGray.main'}}
					>
						Диспетчер
					</Typography>
				</ListItem>
				<ListItem sx={{display:'flex', flexDirection:'row', gap:1}}>
					<Typography component="span" variant="h6">
						Почта:
					</Typography>
					<Typography
						variant="h6"
						sx={{color:'blueGray.main'}}
					>
						toresev@bk.ru
					</Typography>
				</ListItem>

			</List>
			<img src={backlogo} alt="" className='back-logo'/>
		</CustomPaper>
	)
}
