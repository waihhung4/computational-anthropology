import axios from "axios";
import { useEffect, useMemo, useRef, useState } from "react";
import { usePagination, useSortBy, useTable } from "react-table";

const ImageMappingTableComponent = () => {
  const isFirstRender = useRef(true);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [totalPages, setTotalPages] = useState(1);
  const [thresholds, setThresholds] = useState({
    resnet152: 0,
    dinov2: 0,
    ssim: 0,
  });
  const [expandedCells, setExpandedCells] = useState({});
  const [enlargedImage, setEnlargedImage] = useState(null);

  // Helper function to compare thresholds
  const haveThresholdsChanged = (current, next) => {
    return (
      current.resnet152 !== next.resnet152 ||
      current.dinov2 !== next.dinov2 ||
      current.ssim !== next.ssim
    );
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/get_image_mapping?page=1", {
          responseType: "json",
        });
        const processedData = response.data.data.map((item) => ({
          ...item,
          chineseImageUrl: item.chinese_image ? `data:image/png;base64,${item.chinese_image}` : null,
          sumerianImageUrl: item.sumerian_image ? `data:image/png;base64,${item.sumerian_image}` : null,
        }));
        setData(processedData || []);
        setTotalPages(response.data.total_pages || 1);

        const newThresholds = {
          resnet152: response.data.resnet152_threshold || 0,
          dinov2: response.data.dinov2_threshold || 0,
          ssim: response.data.ssim_threshold || 0,
        };
        if (haveThresholdsChanged(thresholds, newThresholds)) {
          setThresholds(newThresholds);
        }
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
      {
        Header: "Chinese Image",
        accessor: "chineseImageUrl",
        disableSortBy: true,
        Cell: ({ value }) => (
          value ? (
            <img
              src={value}
              alt="Chinese Image"
              className="max-w-[100px] max-h-[100px] object-contain rounded-md cursor-pointer"
              onDoubleClick={() => setEnlargedImage(value)}
            />
          ) : (
            <span className="text-gray-400">No Image</span>
          )
        ),
      },
      {
        Header: "Sumerian Image",
        accessor: "sumerianImageUrl",
        disableSortBy: true,
        Cell: ({ value }) => (
          value ? (
            <img
              src={value}
              alt="Sumerian Image"
              className="max-w-[100px] max-h-[100px] object-contain rounded-md cursor-pointer"
              onDoubleClick={() => setEnlargedImage(value)}
            />
          ) : (
            <span className="text-gray-400">No Image</span>
          )
        ),
      },
      {
        Header: "ResNet Similarity",
        accessor: "resnet_similarity_score",
        sortType: "basic",
      },
      {
        Header: "DinoV2 Similarity",
        accessor: "dinov2_similarity_score",
        sortType: "basic",
      },
      {
        Header: "SSIM Similarity",
        accessor: "ssim_similarity_score",
        sortType: "basic",
      },
    ],
    []
  );

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
      manualSortBy: true,
      pageCount: totalPages,
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
        const response = await axios.get(`http://localhost:8000/get_image_mapping?page=${pageIndex + 1}${sortParam}`, {
          responseType: "json",
        });
        const processedData = response.data.data.map((item) => ({
          ...item,
          chineseImageUrl: item.chinese_image ? `data:image/png;base64,${item.chinese_image}` : null,
          sumerianImageUrl: item.sumerian_image ? `data:image/png;base64,${item.sumerian_image}` : null,
        }));
        setData(processedData || []);
        setTotalPages(response.data.total_pages || 1);

        const newThresholds = {
          resnet152: response.data.resnet152_threshold || 0,
          dinov2: response.data.dinov2_threshold || 0,
          ssim: response.data.ssim_threshold || 0,
        };
        if (haveThresholdsChanged(thresholds, newThresholds)) {
          setThresholds(newThresholds);
        }
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [pageIndex, sortBy]);

  if (loading) return <p className="text-white text-lg">Loading...</p>;

  return (
    <div className="p-4 bg-gray-900">
      <div className="mb-6 p-4 bg-gray-800 rounded-lg shadow-lg border border-gray-700">
        <h3 className="text-xl font-semibold text-white mb-4">Similarity Score Thresholds</h3>
        <p className="text-gray-300 mb-4">
          Thresholds represent a reference value calculated as the mean plus one standard deviation (Mean + 1SD) 
          of similarity scores. They help identify how similar images are using each comparison method. 
          Scores above the threshold indicate higher similarity.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="p-4 bg-gradient-to-r from-blue-600 to-blue-400 rounded-md text-white">
            <p className="text-sm font-medium">ResNet152 Threshold</p>
            <p className="text-lg font-bold">{thresholds.resnet152.toFixed(4)}</p>
            <p className="text-xs mt-1">Deep learning-based feature comparison</p>
          </div>
          <div className="p-4 bg-gradient-to-r from-purple-600 to-purple-400 rounded-md text-white">
            <p className="text-sm font-medium">DinoV2 Threshold</p>
            <p className="text-lg font-bold">{thresholds.dinov2.toFixed(4)}</p>
            <p className="text-xs mt-1">Advanced vision transformer comparison</p>
          </div>
          <div className="p-4 bg-gradient-to-r from-green-600 to-green-400 rounded-md text-white">
            <p className="text-sm font-medium">SSIM Threshold</p>
            <p className="text-lg font-bold">{thresholds.ssim.toFixed(4)}</p>
            <p className="text-xs mt-1">Structural similarity comparison</p>
          </div>
        </div>
      </div>

      <table {...getTableProps()} className="w-full border border-gray-700 shadow-md rounded-lg bg-gray-800">
        <thead className="bg-gray-700">
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th
                  {...column.getHeaderProps(column.getSortByToggleProps())}
                  className={`p-3 text-left border border-gray-600 font-semibold text-white ${
                    column.canSort ? "cursor-pointer hover:bg-gray-600" : ""
                  }`}
                >
                  <div className="flex items-center">
                    {column.render("Header")}
                    {column.canSort && (
                      <span className="ml-2">
                        {column.isSorted ? (column.isSortedDesc ? "↓" : "↑") : "↕"}
                      </span>
                    )}
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

      <div className="mt-8">
        <h3 className="text-xl font-semibold text-white mb-4">Similarity Score Distributions</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700">
            <h4 className="text-lg font-medium text-white mb-2">ResNet152 Distribution</h4>
            <img
              src="/images/similarity/resnet.png"
              alt="ResNet152 Similarity Distribution"
              className="w-full h-auto object-contain rounded-md"
            />
          </div>
          <div className="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700">
            <h4 className="text-lg font-medium text-white mb-2">DinoV2 Distribution</h4>
            <img
              src="/images/similarity/dino.png"
              alt="DinoV2 Similarity Distribution"
              className="w-full h-auto object-contain rounded-md"
            />
          </div>
          <div className="bg-gray-800 p-4 rounded-lg shadow-lg border border-gray-700">
            <h4 className="text-lg font-medium text-white mb-2">SSIM Distribution</h4>
            <img
              src="/images/similarity/ssim.png"
              alt="SSIM Similarity Distribution"
              className="w-full h-auto object-contain rounded-md"
            />
          </div>
        </div>
      </div>

      {enlargedImage && (
        <div
          className="fixed inset-0 bg-gray-900 bg-opacity-90 flex items-center justify-center z-50"
          onDoubleClick={() => setEnlargedImage(null)}
        >
          <img src={enlargedImage} alt="Enlarged Image" className="max-w-full max-h-full object-contain" />
        </div>
      )}
    </div>
  );
};

export default ImageMappingTableComponent;