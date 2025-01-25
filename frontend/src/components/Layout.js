import React from 'react';
import CustomNavbar from './Navbar';

function Layout({ children }) {
  return (
    <div>
      {/* Navbar */}
      <CustomNavbar />

      {/* Page Content */}
      <main className="container mt-4">
        {children}
      </main>
    </div>
  );
}

export default Layout;