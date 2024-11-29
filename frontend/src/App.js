import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Navbar from './components/Navbar';
import Products from './components/Products';
import Login from './components/Login';
import Register from './components/Register';
import Cart from './components/Cart';
import { AuthProvider } from './context/AuthContext';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <Router>
          <Navbar />
          <Switch>
            <Route exact path="/" component={Products} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <Route path="/cart" component={Cart} />
          </Switch>
        </Router>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
