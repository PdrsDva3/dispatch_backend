import '../ReportPage/ReportPage';
import { Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';
import React from 'react';
// import { CalendarButton } from '../../../components/CalendarButton/CalendarButton';
import { CalendarDayPage } from '../../CalendarDayPage/CalendarDayPage';



export const ReportPage:React.FC = () => {
	const {date} = useParams<{ date?: string }>();


  return (
    <Container sx={{my:'auto',display:'flex', flexDirection:'column', justifyContent:'space-between', alignItems:'center', backgroundColor:'common.white', gap:4}}>
			<Typography
				variant="h4"
			>
				Отчет за {date}
			</Typography>
			<CalendarDayPage/>
    </Container>
  );
};
