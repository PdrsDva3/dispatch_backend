import { Button, Typography, Box } from "@mui/material"
import loadlogo from '../../assets/svg/dowload.svg'

export const CalendarButton = () => {
	return (
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
	)
}
