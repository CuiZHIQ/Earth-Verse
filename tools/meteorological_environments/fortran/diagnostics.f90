program meteorological_diagnostics
  implicit none
  character(len=64) :: operation
  integer :: n, i
  real(8), allocatable :: values(:)
  real(8) :: du_dx, dv_dy, dv_dx, du_dy
  real(8) :: p1, p2, q1, q2, u1, u2, v1, v2, g

  g = 9.80665d0
  read(*, '(A)') operation

  select case (trim(operation))
  case ('precipitation_summary')
    read(*, *) n
    if (n < 1) stop 2
    allocate(values(n))
    read(*, *) (values(i), i = 1, n)
    write(*, '(4(ES24.16,1X))') sum(values), maxval(values), minval(values), sum(values) / dble(n)
    deallocate(values)
  case ('kinematics')
    read(*, *) du_dx, dv_dy, dv_dx, du_dy
    write(*, '(5(ES24.16,1X))') du_dx + dv_dy, dv_dx - du_dy, &
      du_dx - dv_dy, dv_dx + du_dy, &
      sqrt((du_dx - dv_dy)**2 + (dv_dx + du_dy)**2)
  case ('moisture_transport')
    read(*, *) p1, p2, q1, q2, u1, u2, v1, v2
    write(*, '(4(ES24.16,1X))') &
      -0.5d0 * (q1 + q2) * (p2 - p1) * 100.d0 / g, &
      -0.5d0 * (q1*u1 + q2*u2) * (p2 - p1) * 100.d0 / g, &
      -0.5d0 * (q1*v1 + q2*v2) * (p2 - p1) * 100.d0 / g, &
      sqrt((-0.5d0 * (q1*u1 + q2*u2) * (p2 - p1) * 100.d0 / g)**2 + &
           (-0.5d0 * (q1*v1 + q2*v2) * (p2 - p1) * 100.d0 / g)**2)
  case default
    stop 3
  end select
end program meteorological_diagnostics
