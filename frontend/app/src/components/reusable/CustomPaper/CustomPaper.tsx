import React, { ReactNode } from 'react';
import { Chip, Divider, Grid2, IconButton, Paper } from '@mui/material';
import arrow_right from '../../../assets/svg/arrow-right.svg';
import { useNavigate } from 'react-router-dom';

interface CustomPaperProps {
	title: string;
	children: ReactNode;
	navigationPath?: string;
	className?: string;
	hasButton?: boolean;
}

export const CustomPaper: React.FC<CustomPaperProps> =
	({
		 title,
		 children,
		 navigationPath = '/',
		 className = '',
		 hasButton = true,
	 }) => {
		const navigate = useNavigate();

		const handleSectionClick = () => {
			navigate(navigationPath);
		};

		return (
			<Paper className={[className, 'hover--effect'].join(' ')} elevation={3}
			       sx={{ p: 3, maxWidth: '800px', flexGrow: 1, flexBasis: 1 }}>
				<Grid2 container justifyContent="space-between" alignItems="center" sx={{ mb: 2, minHeight:52 }}>
					<Chip label={title} sx={{ fontSize: 20, borderRadius: '10px' }} component="h2"
					      color="error" />
					{hasButton && <IconButton onClick={handleSectionClick} color="primary">
						<img src={arrow_right} alt="Перейти" />
					</IconButton>}

				</Grid2>
				<Divider sx={{ my: 2 }} />
				{children}
			</Paper>
		);
	};
