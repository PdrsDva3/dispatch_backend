// import { CalendarPaper } from '../../components';
import { Box, Button, Typography } from '@mui/material';
import loadlogo from '../../assets/svg/dowload.svg';
import { DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid';
import { Container } from '@mui/material';


const rows: GridRowsProp = [
	{ id: 1, col1: '0', col2: '0', col3: '0', col4: '0'}
];

const columns: GridColDef[] = [
	{ field: 'col1', headerName: 'Экскаватор', width: 150 },
	{ field: 'col2', headerName: 'Машина', width: 150 },
	{ field: 'col3', headerName: 'Вагон', width: 150 },
	{ field: 'col4', headerName: 'Рабочий', width: 150 },
];

export const CalendarDayPage = () => {
	return (
		<Container  sx={{  my:'auto', display: 'flex', gap:2}}>
			{/* <CalendarPaper hasButton={false} onDateSelect={(date: string) => `/reports/${date}`}/> */}
			<Box sx={{ display: 'flex', flexDirection: 'column', gap:2}}>
				<Box sx={{ display: 'flex', gap: 2}}>
					<Button
						variant="contained"
						sx={{ display: 'flex', gap: 1, color: 'common.white', backgroundColor:"common.white"}}
					>
						<img src={loadlogo} alt="" />
						<Typography variant="h6" sx={{backgroundColor:"common.white"}} color="secondary.dark">
							Скачать
						</Typography>
					</Button>

					<Button
						variant="contained"
						sx={{ display: 'flex', gap: 1, color: 'common.white', backgroundColor:"common.white" }}
					>
						<img src={loadlogo} alt="" />
						<Typography variant="h6" sx={{backgroundColor:"common.white"}} color="secondary.dark">
							Краткий отчёт
						</Typography>
					</Button>
				</Box>

				<DataGrid sx={{ color: 'common.black'}} rows={rows} columns={columns} />
			</Box>
		</Container>
	);
};
