// import { CalendarPaper } from '../../components';
import { Box, Button, Typography } from '@mui/material';
import loadlogo from '../../assets/svg/dowload.svg';
import { DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid';
import { Container } from '@mui/material';


const rows: GridRowsProp = [
	{ id: 1, col1: 'Hello', col2: 'World' },
	{ id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
	{ id: 3, col1: 'MUI', col2: 'is Amazing' },
	{ id: 4, col1: 'DataGridPro', col2: 'is Awesome' },
];

const columns: GridColDef[] = [
	{ field: 'col1', headerName: 'Column 1', width: 150 },
	{ field: 'col2', headerName: 'Column 2', width: 150 },
	{ field: 'col3', headerName: 'Column 3', width: 150 },
	{ field: 'col4', headerName: 'Column 4', width: 150 },
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
