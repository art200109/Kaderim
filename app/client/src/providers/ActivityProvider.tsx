import { createContext, useState, useContext, ReactNode } from 'react';

const ActivityContext = createContext({});

export const ActivityProvider = ({ children }) => {
  const [gender, setGender] = useState([]);
  const [role, setRole] = useState([]);
  const [location, setLocation] = useState([]);
  const [rank, setRank] = useState([]);

  return (
    <ActivityContext.Provider
      value={{
        rank,
        setRank,
        location,
        setLocation,
        role,
        setRole,
        setGender,
        gender
      }}>
      {children}
    </ActivityContext.Provider>
  );
};

export const useActivity = () => useContext(ActivityContext);
