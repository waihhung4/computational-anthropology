import { useState } from "react";
import { NavLink, useLocation } from "react-router-dom";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false); // For mobile menu toggle
  const [isResultsHover, setIsResultsHover] = useState(false); // For results dropdown
  const location = useLocation(); // Get current URL location

  const navItems = [
    { name: "Home", path: "/" },
    { name: "About", path: "/about" },
    { name: "Methodology", path: "/methodology" },
    {
      name: "Results",
      submenu: [
        { name: "URL", path: "/results/url" },
        { name: "Content", path: "/results/content" },
        { name: "Image Mapping", path: "/results/imageMapping" },
        { name: "Word Cloud", path: "/results/wordcloud" },
      ],
    },
    { name: "Data Visualization", path: "/visualization" },
  ];

  const isResultsActive = navItems
    .find((item) => item.name === "Results")
    ?.submenu.some((subItem) => location.pathname === subItem.path);

  return (
    <nav className="fixed top-0 left-0 w-full bg-gray-900 shadow-xl z-50">
      <div className="max-w-screen-xl mx-auto px-6 py-4 flex items-center justify-between">
        <NavLink to="/" className="text-2xl font-extrabold text-white tracking-tight">
          <span className="bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
            CompAnthro
          </span>
        </NavLink>

        <div className="hidden md:flex space-x-6 relative">
          {navItems.map((item) => (
            <div
              key={item.name}
              className="relative"
              onMouseEnter={() => item.submenu && setIsResultsHover(true)}
              onMouseLeave={() => item.submenu && setIsResultsHover(false)}
            >
              <NavLink
                to={item.path}
                className={({ isActive }) =>
                  `text-white px-4 py-2 rounded-lg text-lg font-semibold transition-all duration-300 ${
                    (isActive && !item.submenu) || (item.name === "Results" && isResultsActive)
                      ? "bg-indigo-600 shadow-lg"
                      : "hover:bg-gray-800 hover:shadow-md"
                  }`
                }
              >
                {item.name}
              </NavLink>

              {/* Dropdown for Results */}
              {item.submenu && isResultsHover && (
                <div className="absolute left-0 mt-2 w-48 bg-gray-800 rounded-lg shadow-xl z-10">
                  {item.submenu.map((subItem) => (
                    <NavLink
                      key={subItem.name}
                      to={subItem.path}
                      className={({ isActive }) =>
                        `block px-4 py-2 text-white text-sm font-medium transition-all duration-200 ${
                          isActive ? "bg-indigo-600" : "hover:bg-gray-700"
                        }`
                      }
                    >
                      {subItem.name}
                    </NavLink>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;