import { AppBar, Button, Toolbar, Box } from '@mui/material';
import './Header.scss'
import logo from '../../../assets/svg/newrgd.svg'
import headerline from '../../../assets/svg/red-line-header.svg'
import logout from '../../../assets/svg/logout.svg'
import '../../../theme.ts'
import { NavLink, useNavigate } from 'react-router-dom';



export const Header = () => {
	const navigate = useNavigate();

	return (
		<AppBar className='app-bar'
			sx={{height:"10vh", position:"sticky", top:0, width:"100%", color:"common.white", backgroundColor:"common.white", mb:"1vh"}}
		>

			<Toolbar className='toolbar' sx={{ display: 'flex', gap:3, justifyContent:"space-between"}}>
				<Box sx={{ display: 'flex', gap:3, justifyContent:"space-between"}}>
					<NavLink to="/">
						<img src={logo} alt="" className="logo" />
					</NavLink>
					<Box sx={{ display: 'flex', gap:3, justifyContent:"space-between"}}>
						<Button
							variant='text'
							sx={{color:"common.black"}}

						>
							<NavLink to="/">
								Главная
							</NavLink>
						</Button>

						<Button
							variant='text'
							sx={{color:'common.black'}}
						>
							<NavLink to="/monitoring">
								Мониторинг
							</NavLink>
						</Button>

						<Button
							variant='text'
							sx={{color:'common.black'}}
						>
							<NavLink to="/reports">
								Календарь отчетов
							</NavLink>
						</Button>

					</Box>
				</Box>


				<Button sx={{color:'common.black', alignSelf:"self-start"}} onClick={() => navigate("/login")}>
					<img src={logout} alt="" />
				</Button>
			</Toolbar>

			<img className='red-line' src={headerline} alt="" />
		</AppBar>
	);
};
