import React, { useState } from 'react';
import { Dayjs } from 'dayjs';
import { DemoContainer } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar';
import { useNavigate } from 'react-router-dom';

interface CalendarProps {
	onDateSelect: (date: string) => string;
}


export const Calendar: React.FC<CalendarProps> = ({ onDateSelect }) => {
	const [selectedDate, setSelectedDate] = useState<Dayjs | null>(null);
	const navigate = useNavigate();

	const handleDateChange = (date: Dayjs | null) => {
		setSelectedDate(date);
		if (date) {
			const formattedDate = date.format('YYYY-MM-DD');
			const newPath = onDateSelect(formattedDate);
			navigate(newPath);
		}
	};

	return (
		<LocalizationProvider dateAdapter={AdapterDayjs}>
			<DemoContainer components={['DateCalendar']}>
				<DateCalendar
					value={selectedDate}
					onChange={handleDateChange}
					views={['year', 'month', 'day']}
				/>
			</DemoContainer>
		</LocalizationProvider>
	);
};
