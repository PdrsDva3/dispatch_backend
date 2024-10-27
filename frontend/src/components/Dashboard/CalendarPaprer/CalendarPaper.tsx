import React from 'react';
import { CustomPaper } from '../../reusable';
import { Calendar } from './Calendar/Calendar.tsx';
import '../CalendarPaprer/CalendarPaper.scss';

interface CalendarPaperProps {
	hasButton: boolean;
	onDateSelect: (date: string) => string;
}

export const CalendarPaper: React.FC<CalendarPaperProps> = ({ hasButton }) => {
	return (
		<CustomPaper
			title="Календарь отчетов"
			navigationPath="/reports"
			className="elevate--hover"
			hasButton={hasButton}
		>
			<Calendar onDateSelect={(date: string) => `/reports/${date}`} />
		</CustomPaper>
	);
};
