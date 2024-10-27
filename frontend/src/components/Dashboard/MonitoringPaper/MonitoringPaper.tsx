import React from 'react';
import { CustomPaper } from '../../reusable';
import backlogo from '../../../assets/svg/backCamera.svg';
import '../../Dashboard/MonitoringPaper/MonitoringPaper.scss';

export const MonitoringPaper: React.FC = () => {
	return (
		<CustomPaper
			title="Мониторинг"
			className="monitoring__paper elevate--hover"
			navigationPath = '/monitoring'
		>
				<img src={backlogo} alt="" className='back-logo' />
		</CustomPaper>
	)
}
