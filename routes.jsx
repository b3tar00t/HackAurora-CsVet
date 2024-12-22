import { createBrowserRouter, RouterProvider } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import AuthPage from "./pages/AuthPage";
import Dashboard from "./pages/Dashboard";

const router = createBrowserRouter([
  { path: "/", element: <LandingPage /> },
  { path: "/auth", element: <AuthPage /> },
  { path: "/dashboard", element: <Dashboard /> },
]);

const Routes = () => <RouterProvider router={router} />;
export default Routes;
