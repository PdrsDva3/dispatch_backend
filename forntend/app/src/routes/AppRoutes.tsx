import { Route, Routes } from 'react-router-dom';
import {
	DashboardPage,
	LoginPage,
	MainLayout,
	MonitoringPage, NotFoundPage,
	ReportsPage,
} from '../pages';
import {ReportPage} from '../pages/ReportsPage/ReportPage/ReportPage'
import { Header } from '../components';
import { CalendarDayPage } from '../pages/CalendarDayPage/CalendarDayPage';

export const AppRoutes = () => {
	return (
		<Routes>
			<Route path='/login' element={<LoginPage/>}/>
			<Route path="/" element={<MainLayout/>} >
				<Route index element={<DashboardPage/>}/>
				<Route path="header" element={<Header/>}/>
				<Route path="monitoring" element={<MonitoringPage/>}/>
				<Route path="reports" element={<ReportsPage/>}>
					<Route path=":date" element={<ReportPage/>}/>
				</Route >
				<Route path="calendar" element={<CalendarDayPage/>}/>
			</Route>
			<Route path="*" element={<NotFoundPage/>}/>
		</Routes>
	);
};
