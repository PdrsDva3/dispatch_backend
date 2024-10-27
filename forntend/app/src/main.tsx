import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App.tsx';
import './styles/index.css';
import './styles/variables.css';
import './styles/normalize.css';
import './styles/fonts.css';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';
import { store } from './redux/store.ts';
import { CssBaseline, ThemeProvider } from '@mui/material';
import { theme } from './theme.ts';


createRoot(document.getElementById('root')!).render(
	<StrictMode>
		<Provider store={store}>
			<ThemeProvider theme={theme}>
				<CssBaseline />
					<BrowserRouter>
						<App />
					</BrowserRouter>
			</ThemeProvider>
		</Provider>
	</StrictMode>,
);
