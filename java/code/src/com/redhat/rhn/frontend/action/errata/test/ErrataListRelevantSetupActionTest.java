/**
 * Copyright (c) 2009 Red Hat, Inc.
 *
 * This software is licensed to you under the GNU General Public License,
 * version 2 (GPLv2). There is NO WARRANTY for this software, express or
 * implied, including the implied warranties of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
 * along with this software; if not, see
 * http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
 *
 * Red Hat trademarks are not licensed under GPLv2. No permission is
 * granted to use or replicate Red Hat trademarks that are incorporated
 * in this software or its documentation. 
 */
package com.redhat.rhn.frontend.action.errata.test;

import com.redhat.rhn.frontend.action.errata.ErrataListRelevantSetupAction;
import com.redhat.rhn.testing.ActionHelper;
import com.redhat.rhn.testing.RhnBaseTestCase;

/**
 * ErrataListRelevantSetupActionTest
 * @version $Rev$
 */
public class ErrataListRelevantSetupActionTest extends RhnBaseTestCase {
    
    public ErrataListRelevantSetupActionTest(String name) {
        super(name);
    }
    
    public void testExecute() throws Exception {
        ErrataListRelevantSetupAction action = new ErrataListRelevantSetupAction();
        ActionHelper ah = new ActionHelper();
        
        ah.setUpAction(action);
        ah.setupClampListBounds();
        
        ah.executeAction();
        
        assertNotNull(ah.getRequest().getAttribute("pageList"));
    }
}
