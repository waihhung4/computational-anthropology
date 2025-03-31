import axios from "axios";
import { useEffect, useMemo, useRef, useState } from "react";
import { usePagination, useSortBy, useTable } from "react-table";

const ContentTableComponent = () => {
  const isFirstRender = useRef(true);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [totalPages, setTotalPages] = useState(1);
  const [expandedCells, setExpandedCells] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/get_url?page=1");
        setData(response.data.data || []);
        setTotalPages(response.data.total_pages || 1);
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const columns = useMemo(
    () => [
      { Header: "URL", accessor: "url" },
      { Header: "Search Keyword", accessor: "search_keyword" },
      { Header: "Source", accessor: "source" },
    ],
    []
  ); // Removed expandedCells dependency since it’s not used here

  const toggleExpand = (rowIndex, columnId) => {
    setExpandedCells((prev) => {
      const key = `${rowIndex}-${columnId}`;
      return { ...prev, [key]: !prev[key] };
    });
  };

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    page: tablePage,
    prepareRow,
    canPreviousPage,
    canNextPage,
    nextPage,
    previousPage,
    state: { pageIndex, sortBy },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0, pageSize: 10 },
      manualPagination: true,
      pageCount: totalPages,
      manualSortBy: true,
    },
    useSortBy,
    usePagination
  );

  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    const fetchData = async () => {
      setLoading(true);
      try {
        const sortParam = sortBy.length > 0 ? `&sortBy=${sortBy[0].id}&order=${sortBy[0].desc ? "desc" : "asc"}` : "";
        const response = await axios.get(`http://localhost:8000/get_url?page=${pageIndex + 1}${sortParam}`);
        setData(response.data.data || []);
        setTotalPages(response.data.total_pages || 1);
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [pageIndex, sortBy]); // Add sortBy as a dependency

  if (loading) return <p className="text-white text-lg">Loading...</p>;

  return (
    <div className="p-4 bg-gray-900">
      <table {...getTableProps()} className="w-full border border-gray-700 shadow-md rounded-lg bg-gray-800">
        <thead className="bg-gray-700">
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th
                  {...column.getHeaderProps(column.getSortByToggleProps())} // Add sorting props
                  className="p-3 text-left border border-gray-600 font-semibold text-white cursor-pointer hover:bg-gray-600"
                >
                  <div className="flex items-center">
                    {column.render("Header")}
                    {/* Sort direction indicators */}
                    <span className="ml-2">
                      {column.isSorted ? (column.isSortedDesc ? "↓" : "↑") : "↕"}
                    </span>
                  </div>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {tablePage.map((row, rowIndex) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()} className="hover:bg-gray-600">
                {row.cells.map((cell) => {
                  const key = `${rowIndex}-${cell.column.id}`;
                  const isExpanded = expandedCells[key];
                  return (
                    <td
                      {...cell.getCellProps()}
                      className={`p-3 border border-gray-700 cursor-pointer transition-all duration-200 text-white ${
                        isExpanded ? "whitespace-normal" : "truncate overflow-hidden max-w-xs"
                      }`}
                      onDoubleClick={() => toggleExpand(rowIndex, cell.column.id)}
                    >
                      <div
                        className={
                          isExpanded
                            ? "absolute bg-gray-800 p-2 shadow-lg border border-gray-700 rounded-md z-10 text-white"
                            : "truncate overflow-hidden max-w-xs"
                        }
                      >
                        {cell.render("Cell")}
                      </div>
                    </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
      <div className="flex justify-between items-center mt-4 text-white">
        <button
          onClick={previousPage}
          disabled={!canPreviousPage}
          className="px-4 py-2 bg-gray-700 text-white rounded hover:bg-gray-600 disabled:opacity-50"
        >
          Previous
        </button>
        <span>
          Page {pageIndex + 1} of {totalPages}
        </span>
        <button
          onClick={nextPage}
          disabled={!canNextPage}
          className="px-4 py-2 bg-gray-700 text-white rounded hover:bg-gray-600 disabled:opacity-50"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ContentTableComponent;