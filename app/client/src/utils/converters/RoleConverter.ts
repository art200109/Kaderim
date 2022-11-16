import { Role } from '../../../../common/types/enums';

export const RoleConverter = {
  [Role.Mandatory]: 'חייל חובה',
  [Role.Officer]: 'קצין',
  [Role.Nagad]: 'נגד'
};
