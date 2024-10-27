import { Container, Typography } from '@mui/material';
import { Outlet, useParams } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import { CalendarPaper } from '../../components';

export const ReportsPage: React.FC= () => {
  const { date } = useParams<{ date?: string }>();
  const [showSelectDate, setShowSelectDate] = useState<boolean>(true);

  useEffect(() => {
    setShowSelectDate(!date);
  }, [date]);

  return (
    <Container sx={{ height: 1, display: "flex", my: 'auto' }}>
      <CalendarPaper hasButton={false} onDateSelect={(date: string) => `/reports/${date}`} />
      <Outlet />
      {showSelectDate && (
        <Container
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center'
          }}
        >
          <Typography
            variant='h3'
            sx={{ color: 'secondary.dark' }}
          >
            Выберите дату
          </Typography>
        </Container>
      )}
    </Container>
  );
};

